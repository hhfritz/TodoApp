import 'dart:async';
import 'package:flutter/material.dart';

class AuthService with ChangeNotifier {
  var currentuser;

  AuthService() {
    print("new AuthService");
  }

  Future getUser() {
    return Future.value(currentuser);
  }

  Future logout() {
    this.currentuser = null;
    notifyListeners();
    return Future.value(currentuser);
  }

  Future createUser(
    {String firstname,
    String lastName,
    String email,
    String password}
  ) async {}

  Future loginUser({String email, String password}) {
    if (password == 'password123') {
        this.currentuser = {'email' : email};
        notifyListeners();
        return Future.value(currentuser);
    } else {
      this.currentuser = null;
      return Future.value(null);
    }
  }
}