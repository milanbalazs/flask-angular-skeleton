import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PingComponent } from './pages/ping/ping.component';
import { HomeComponent } from './pages/home/home.component';

const routes: Routes = [
  {
    path: 'ping',
    component: PingComponent
  },
  {
    path: '**',
    component: HomeComponent
  }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
