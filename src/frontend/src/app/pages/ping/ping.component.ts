import { Component, OnInit } from '@angular/core';
import { Ping } from '../../models/ping.model';
import { PingService } from '../../services/ping.service';

@Component({
  selector: 'app-ping',
  templateUrl: './ping.component.html',
  styleUrls: ['./ping.component.css']
})
export class PingComponent implements OnInit {

  todayDate : Date = new Date();
  ping: Ping;

  ngOnInit() {
    this.pingService.getPing().subscribe(ping => {
      this.ping = ping;
    });
  }

  ngAfterViewInit() {
  }

  constructor(private pingService: PingService) {}

}
