import 'package:flutter/material.dart';

class KeyPad extends StatelessWidget {
    // final append
    const KeyPad({Key? key, required this.appendTextCallback, required this.appendCurrent}) : super(key: key);
    final Function appendTextCallback;
    final Function appendCurrent;
    @override
    Widget build(BuildContext context) {
        // ignore: non_constant_identifier_names
        List<String> numbers__ = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ".",
            "0",
            "=",
        ];

        Map<String, Function> numbers_ = {
            for (var e in numbers__)
                e: () {
                    appendTextCallback(e);
                }
        };
        numbers_["="] = (){appendCurrent();};
        
        // "←", "→", "del", "clr"
        var ops_ = [
            "(",
            ")",
            "+",
            "-",
            "*",
            "/",
            "sqrt",
            "^",
            "e",
            "sin",
            "cos",
            "pi",
        ];

          Map<String, Function> ops = {
            for (var e in ops_)
                e: () {
                    appendTextCallback(e);
                }
        };

        GridView operations = makeButtonGroup(ops);

        GridView numbers = makeButtonGroup(numbers_);

        const others = ["prev", "<-", "->", "del", "clr"];

        Row otherButtons = Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: others
                    .map((e) => OutlinedButton(
                            onPressed: () {},
                            child: Text(
                                e,
                                style: const TextStyle(fontSize: 25),
                            )))
                    .toList(),
        );

        //sqrt, pow, e/pi, +, -, *, /, ()
        return Column(
            children: [
                otherButtons,
                Flexible(
                        child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                        Flexible(child: numbers),
                        Container(
                            color: Colors.blue[200],
                            width: 2,
                            height: 300,
                            margin: const EdgeInsets.symmetric(vertical: 0, horizontal: 5),
                        ),
                        Flexible(child: operations),
                    ],
                ))
            ],
        );
    }

    GridView makeButtonGroup(Map<String, Function> items) {
        return GridView.builder(
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3),
                itemCount: items.length,
                shrinkWrap: true,
                itemBuilder: (_, index) {
                    String key = items.keys.elementAt(index);
                    return OutlinedButton(
                            onPressed: () => items[key]!(),
                            child: Text(
                                key,
                                style: const TextStyle(fontSize: 25),
                            ));
                });
    }
}
