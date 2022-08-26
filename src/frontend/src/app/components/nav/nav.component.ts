import { Component, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  toolbarTitle: string;

  isHandset$: Observable<boolean> = this.breakpointObserver
    .observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  ngOnInit(): void {}

  constructor(
    private breakpointObserver: BreakpointObserver,
    private router: Router,
  ) {
    this.router.events.subscribe((event: any) => {
      if (event instanceof NavigationEnd) {
        this.toolbarTitle = this.router.url.replace('/', '');
        if (!this.toolbarTitle) {
          this.toolbarTitle = 'Home';
        }
        else {
          this.toolbarTitle = this.toolbarTitle.toUpperCase( );
        }
      }
    });
  }


  onLogout() {
    console.log('Logout');
  }
}
