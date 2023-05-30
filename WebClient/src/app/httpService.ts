import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { SourceText } from "./types";
import { Observable } from "rxjs";
import { env } from "./env";

const buildUrl = (url: string) => {
  return env.SERVER_URL + url;
}

@Injectable()
export class HttpService {
  constructor(private http: HttpClient) { }

  convertText(options: SourceText): Observable<any> {
    return this.http.post<SourceText>(buildUrl('/convert/'), options);
  }
}
