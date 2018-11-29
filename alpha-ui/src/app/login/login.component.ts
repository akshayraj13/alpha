import {Component, OnInit} from '@angular/core';
import {FormGroup} from '@angular/forms';
import {LoginModel} from 'app/_models';
import {LoginForm} from 'app/_forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit{
  public loginForm: FormGroup;
  loginInfo: LoginModel = <LoginModel>{};

  constructor() {}

  ngOnInit() {
    this.loginForm = LoginForm.createForm(this.loginInfo);
  }
  doLogin() {
    console.log(this.loginForm.value);
  }
}
