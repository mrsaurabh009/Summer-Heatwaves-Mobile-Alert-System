import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;


void main() {
  runApp(const HeatwaveApp());
}

class HeatwaveApp extends StatelessWidget {
  const HeatwaveApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Heatwave Alert System',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.deepOrange),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String message = "Loading...";
  bool isLoading = true;
  bool isHeatwave = false;
  double temperature = 0.0;

  @override
  void initState() {
    super.initState();
    fetchHeatwaveData();
  }

  Future<void> fetchHeatwaveData() async {
    try {
      final response = await http.get(
        Uri.parse('https://heatwave-alert-system-3.onrender.com/predict'),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          temperature = data['temperature'];
          isHeatwave = data['is_heatwave'];
          message = data['message'];
          isLoading = false;
        });
      } else {
        setState(() {
          message = "Failed to load data";
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        message = "Error fetching data: $e";
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("🔥 Heatwave Alert")),
      body: Center(
        child: isLoading
            ? const CircularProgressIndicator()
            : Padding(
                padding: const EdgeInsets.all(20.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text("🌡️ Temperature: ${temperature.toStringAsFixed(1)}°C",
                        style: const TextStyle(fontSize: 24)),
                    const SizedBox(height: 20),
                    Text(
                      message,
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 22,
                        color: isHeatwave ? Colors.red : Colors.green,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 30),
                    ElevatedButton(
                      onPressed: fetchHeatwaveData,
                      child: const Text("🔄 Refresh"),
                    ),
                  ],
                ),
              ),
      ),
    );
  }
}

