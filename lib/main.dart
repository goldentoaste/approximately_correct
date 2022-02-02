import 'package:flutter/material.dart';

void main() {
    runApp(const MyApp());
}

class MyApp extends StatelessWidget {
    const MyApp({Key? key}) : super(key: key);

    // This widget is the root of your application.
    @override
    Widget build(BuildContext context) {
        return MaterialApp(
            title: "wow!",
            home: Scaffold(
                appBar: AppBar(
                    title: const Text("help"),
                ),
                body: const Center(
                    child: Text("body body bdoy"),
                ),
            ),
        );
    }
}
