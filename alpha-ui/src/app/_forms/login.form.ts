import {LoginModel} from 'app/_models';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

export class LoginForm {
  static loginForm: FormGroup;

  static createForm(loginInfo: LoginModel, formBuilder: FormBuilder = new FormBuilder()): FormGroup {
    this.loginForm = formBuilder.group({
      userName: [loginInfo.userName, Validators.required],
      password: [loginInfo.password, Validators.required]
    });
    return this.loginForm;
  }
}
