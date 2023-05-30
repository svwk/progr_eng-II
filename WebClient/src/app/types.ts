export interface SourceText {
  text: string | null;
  precision: number | null;
}

export interface ConvertResponse {
  generated_text: string;
}
