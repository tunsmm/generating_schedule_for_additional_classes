import { NgDompurifySanitizer } from "@tinkoff/ng-dompurify";
import {
    TuiRootModule,
    TuiDialogModule,
    TuiAlertModule,
    TUI_SANITIZER,
    TuiButtonModule,
    TuiLinkModule, TuiThemeNightModule, TuiModeModule, TuiErrorModule, TuiLoaderModule
} from "@taiga-ui/core";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { FileLoadingComponent } from './file-loading/file-loading.component';
import {
  TuiCheckboxModule,
  TuiFieldErrorPipeModule,
  TuiInputFilesModule,
  TuiIslandModule,
  TuiToggleModule
} from "@taiga-ui/kit";
import {ReactiveFormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    FileLoadingComponent
  ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        TuiRootModule,
        TuiDialogModule,
        TuiAlertModule,
        TuiIslandModule,
        TuiButtonModule,
        TuiToggleModule,
        ReactiveFormsModule,
        TuiLinkModule,
        TuiCheckboxModule,
        TuiThemeNightModule,
        TuiModeModule,
        TuiInputFilesModule,
        TuiErrorModule,
        TuiFieldErrorPipeModule,
        TuiLoaderModule
    ],
  providers: [{provide: TUI_SANITIZER, useClass: NgDompurifySanitizer}],
  bootstrap: [AppComponent]
})
export class AppModule { }
