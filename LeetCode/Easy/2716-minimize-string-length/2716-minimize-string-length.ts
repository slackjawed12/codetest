function minimizedStringLength(s: string): number {
  return Array.from(new Set(s.split(""))).length;
}
