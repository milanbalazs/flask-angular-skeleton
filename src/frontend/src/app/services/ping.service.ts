import { Injectable } from '@angular/core';
import { Ping } from '../models/ping.model';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PingService {
  constructor(private http: HttpClient) {}

  getPing(): Observable<Ping> {
    return this.http.get<Ping>(`${environment.apiUrl}/ping`);
  }
}
