import 'package:flutter/material.dart';

// ignore: must_be_immutable
class IOFields extends StatefulWidget {
     IOFields({Key? key, required this.items, required this.current}) : super(key: key);
     List<String> items;
     String current;
    static of(BuildContext context) => context.findAncestorStateOfType<_IOFieldsState>();


    @override
    _IOFieldsState createState() => _IOFieldsState();
}

class _IOFieldsState extends State<IOFields> {

    //todo implement cursor locations
    @override
    Widget build(BuildContext context) {
        return Column(
            // crossAxisAlignment: CrossAxisAlignment.center,
            children: [
                Expanded(
                    child: ListView.builder(
                        itemCount: widget.items.length * 2,
                        reverse: true,
                        itemBuilder: (context, index) {
                            if (index.isOdd) {
                                return const Divider();
                            }
                            return Text(
                                widget.items[index ~/ 2],
                                textAlign: TextAlign.right,
                                style:
                                        const TextStyle(color: Colors.black87, fontSize: 25, fontFamily: 'Courier'),
                            );
                        }),
                ),
                TextField(
                    readOnly: true,
                    controller: TextEditingController(text: widget.current),
                    decoration: const InputDecoration(
                        
                            border: null, hintText: "use the key pad below to start typing", hintMaxLines: 1),
                    maxLines: 1,
                    scrollController: ScrollController(),
                    textAlign: TextAlign.right,
                    style: const TextStyle(color: Colors.black87, fontSize: 25, fontFamily: 'Courier'),
                )
            ],
        );
    }

    // void equals(){
    //     widget.items.add(currentInput);
    //     currentInput = "";
    // }
}
