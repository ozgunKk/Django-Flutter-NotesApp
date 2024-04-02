import 'package:flutter/material.dart';
import 'package:http/http.dart';

class CreatePage extends StatefulWidget {
  final Client client;
  const CreatePage({
    Key? key,
    required this.client,
  }) : super(key: key);

  @override
  State<CreatePage> createState() => _CreatePageState();
}

class _CreatePageState extends State<CreatePage> {
  TextEditingController controller = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Create Note'),
      ),
    );
  }
}
