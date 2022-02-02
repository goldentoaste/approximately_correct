import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart' as words;

void main() {
    runApp(const MyApp());
}

class MyApp extends StatelessWidget {
    const MyApp({Key? key}) : super(key: key);

    // This widget is the root of your application.
    @override
    Widget build(BuildContext context) {
        return const MaterialApp(
            title: "wow!",
            home: RngWords(),
        );
    }
}

class OtherPage extends StatelessWidget {
    const OtherPage(this.savedItems, {Key? key}) : super(key: key);

    final Set<words.WordPair> savedItems;

    @override
    Widget build(BuildContext context) {
        final tiles = savedItems.map((pair) => ListTile(
                    title: Text(
                        pair.asPascalCase,
                        style: const TextStyle(fontSize: 25),
                    ),
                ));

        final divided = tiles.isNotEmpty
                ? ListTile.divideTiles(context: context, tiles: tiles).toList()
                : <Widget>[];

        return MaterialApp(
            title: "the other page!",
            home: Scaffold(
                    appBar: AppBar(
                        title: const Text("the other other"),
                    ),
                    body: ListView(
                        children: divided,
                    )),
        );
    }
}


class RngWords extends StatefulWidget {
    const RngWords({Key? key}) : super(key: key);

    @override
    _RngWordsState createState() => _RngWordsState();
}

class _RngWordsState extends State<RngWords> {
    final _suggestions = <words.WordPair>[];
    final _saved = <words.WordPair>{};
    static const _font = TextStyle(fontSize: 25, color: Colors.blue);

    void _moveToSaved() {
        Navigator.of(context)
                .push(MaterialPageRoute(builder: OtherPage(_saved).build));
    }

    @override
    Widget build(BuildContext context) {
        return Scaffold(
            appBar: AppBar(
                title: const Text(
                    "help gelphelp helphelp",
                ),
                actions: [
                    IconButton(onPressed: _moveToSaved, icon: const Icon(Icons.list))
                ],
            ),
            body: _buildSuggestons(),
        );
    }

    Widget _buildSuggestons() {
        return ListView.builder(
            padding: const EdgeInsets.all(16),
            itemBuilder: (context, index) {
                if (index.isOdd) {
                    return const Divider();
                }
                final i = index ~/ 2; //integer division

                if (index >= _suggestions.length) {
                    _suggestions.addAll(words.generateWordPairs().take(10));
                }
                return _buildRow(_suggestions[i]);
            },
        );
    }

    Widget _buildRow(words.WordPair pair) {
        final alreadySaved = _saved.contains(pair);
        return ListTile(
            title: Text(pair.asPascalCase, style: _font),
            trailing: IconButton(
                icon: Icon(
                    alreadySaved ? Icons.favorite : Icons.favorite_border_outlined,
                    color: alreadySaved ? Colors.red : null,
                    semanticLabel: alreadySaved ? "remove" : "save",
                ),
                onPressed: () {
                    //lambda function
                    setState(() {
                        if (alreadySaved) {
                            _saved.remove(pair);
                        } else {
                            _saved.add(pair);
                        }
                    });
                },
            ),
            onTap: () {},
        );
    }
}
