import 'package:flutter/material.dart';

class IOFields extends StatefulWidget {
    const IOFields({Key? key}) : super(key: key);

    static of(BuildContext context) => context.findAncestorStateOfType<_IOFieldsState>();

    @override
    _IOFieldsState createState() => _IOFieldsState();
}

class _IOFieldsState extends State<IOFields> {
    final previousResults = <String>[];
    static var currentInput = "";
    @override
    Widget build(BuildContext context) {
        return Column(
            // crossAxisAlignment: CrossAxisAlignment.center,
            children: [
                Expanded(
                    child: ListView.builder(
                            itemCount: previousResults.length,
                            reverse: true,
                            itemBuilder: (context, index) {
                                if (index.isOdd) {
                                    return const Divider();
                                }

                                return Text(
                                    previousResults[index],
                                    textAlign: TextAlign.right,
                                    style:
                                            const TextStyle(color: Colors.black87, fontSize: 20, fontFamily: 'Courier'),
                                );
                            }),
                ),
                TextField(
                    decoration: const InputDecoration(
                        
                            border: null, hintText: "use the key pad below to start typing", hintMaxLines: 1),
                    maxLines: 1,
                    scrollController: ScrollController(),
                    textAlign: TextAlign.right,
                    style: const TextStyle(color: Colors.black87, fontSize: 20, fontFamily: 'Courier'),
                )
            ],
        );
    }

     void update(){
        setState(() {
          //pass, just to force a re-render
        });
    }

    void equals(){
        previousResults.add(currentInput);
        currentInput = "";
    }
}
