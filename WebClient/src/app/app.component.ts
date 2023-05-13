import { Component } from '@angular/core';
import { HttpService } from "./httpService";
import { FormControl, FormGroup, Validators } from "@angular/forms";
import { ConvertResponse } from "./types";

const MIN_PRECISION = 0.01;
const MAX_PRECISION = 0.99;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [HttpService]
})
export class AppComponent {
  MIN_PRECISION: number = MIN_PRECISION;
  MAX_PRECISION: number = MAX_PRECISION;
  result: string = '';
  error: string = '';
  isLoading: boolean = false;
  didRequest: boolean = false;
  form: FormGroup = new FormGroup({
    text: new FormControl<string>('', [
      Validators.required
    ]),
    precision: new FormControl<number>(0.95, [
      Validators.required,
      Validators.min(MIN_PRECISION),
      Validators.max(MAX_PRECISION)
    ]),
  });

  constructor(
    private httpService: HttpService,
  ) {}

  get text() { return this.form.get('text'); }

  get precision() { return this.form.get('precision'); }

  onSubmit(): void {
    if (this.form.invalid) {
      this.form.markAsTouched();
      this.form.controls['text'].markAsTouched();
      this.form.controls['precision'].markAsTouched();
      return;
    }
    this.isLoading = true;
    this.didRequest = false;
    this.result = '';
    this.httpService.convertText({
      text: this.text?.value || null,
      precision: this.precision?.value || null,
    }).subscribe(
    (data: ConvertResponse) => {
      this.result = data.generated_text;
      this.error = '';
      this.isLoading = false;
      this.didRequest = true;
    },
    (error) => {
      this.error = 'API error. API is not available';
      this.isLoading = false;
      this.didRequest = true;
    }
    )
  }
}
