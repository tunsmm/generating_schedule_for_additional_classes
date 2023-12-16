import {Component, Inject} from '@angular/core';
import {AbstractControl, FormControl, ValidatorFn} from "@angular/forms";
import {TuiFileLike} from "@taiga-ui/kit";
import {TuiValidationError} from "@taiga-ui/cdk";
import {TuiAlertService} from "@taiga-ui/core";
import {BehaviorSubject, Subject} from "rxjs";

@Component({
  selector: 'app-file-loading',
  templateUrl: './file-loading.component.html',
  styleUrls: ['./file-loading.component.less']
})
export class FileLoadingComponent {
  readonly scheduleFormControl = new FormControl([], [maxFilesLength(100)]);
  rejectedScheduleFiles: readonly TuiFileLike[] = [];

  readonly studentsFormControl = new FormControl([], [maxFilesLength(100)]);
  rejectedStudentsFiles: readonly TuiFileLike[] = [];

  isLoading$:boolean = false;

  fileSent$: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);

  constructor(@Inject(TuiAlertService) private readonly alerts: TuiAlertService) {
  }

  ngOnInit(): void {
    this.scheduleFormControl.statusChanges.subscribe(response => {
      console.info('STATUS', response);
      console.info('ERRORS', this.scheduleFormControl.errors, '\n');
    });
    this.studentsFormControl.statusChanges.subscribe(response => {
      console.info('STATUS', response);
      console.info('ERRORS', this.studentsFormControl.errors, '\n');
    });
  }

  onScheduleReject(files: TuiFileLike | readonly TuiFileLike[]): void {
    this.rejectedScheduleFiles = [...this.rejectedScheduleFiles, ...(files as TuiFileLike[])];
  }

  onStudentsReject(files: TuiFileLike | readonly TuiFileLike[]): void {
    this.rejectedStudentsFiles = [...this.rejectedStudentsFiles, ...(files as TuiFileLike[])];
  }

  removeScheduleFile({name}: File): void {
    this.scheduleFormControl.setValue(
      this.scheduleFormControl.value?.filter((current: File) => current.name !== name) ?? [],
    );
  }

  removeStudentsFile({name}: File): void {
    this.studentsFormControl.setValue(
      this.studentsFormControl.value?.filter((current: File) => current.name !== name) ?? [],
    );
  }

  clearScheduleRejected({name}: TuiFileLike): void {
    this.rejectedScheduleFiles = this.rejectedScheduleFiles.filter(
      rejected => rejected.name !== name,
    );
  }

  clearStudentsRejected({name}: TuiFileLike): void {
    this.rejectedStudentsFiles = this.rejectedStudentsFiles.filter(
      rejected => rejected.name !== name,
    );
  }

  async sendFiles(): Promise<void> {
    this.isLoading$ = true;
    try {
      for(const item of this.scheduleFormControl.value) {
        const formData = new FormData();
        formData.append('file', item)
        await fetch('http://localhost:8000/uploadfile/schedules',
          {method: 'POST', body: formData})
      }
      this.scheduleFormControl.setValue([]);
      this.alerts.open('Все файлы расписаний успешно загружены!', {label: 'Успешно', autoClose: 10000})
        .subscribe();
    } catch (err) {
      console.log(err)
      this.alerts.open('Файлы расписаний не были загружены', {label: 'Ошибка', autoClose: 10000, status: 'error'})
        .subscribe();
    }
    try {
      for(const item of this.studentsFormControl.value) {
        const formData = new FormData();
        formData.append('file', item)
        await fetch('http://localhost:8000/uploadfile/studentsGroups',
          {method: 'POST', body: formData})
      }
      this.studentsFormControl.setValue([]);
      this.alerts.open('Все файлы групп студентов успешно загружены!', {label: 'Успешно', autoClose: 10000})
        .subscribe();
    } catch (err) {
      console.log(err)
      this.alerts.open('Файлы групп студентов не были загружены', {label: 'Ошибка', autoClose: 10000, status: 'error'})
        .subscribe();
    }
    this.isLoading$ = false;
    this.fileSent$.next(true);
  }

  async downloadResult() {
    try {
      await fetch('http://localhost:8000/generate_schedule/', {method: 'GET'})
        .then(data => data.blob())
        .then((data) => this.download(data, 'result_schedule.xlsx'));
    } catch (err) {
      console.log(err)
    }
  }

  async download(data: Blob, filename: any) {
    const objectUrl = URL.createObjectURL(data)
    const link = document.createElement('a')

    link.setAttribute('href', objectUrl)
    link.setAttribute('download', filename)
    link.style.display = 'none'

    document.body.appendChild(link)

    link.click()

    document.body.removeChild(link)
  }
}

export function maxFilesLength(maxLength: number): ValidatorFn {
  return ({value}: AbstractControl) =>
    value.length > maxLength
      ? {
        maxLength: new TuiValidationError(
          'Error: maximum limit - 5 files for upload',
        ),
      }
      : null;
}
