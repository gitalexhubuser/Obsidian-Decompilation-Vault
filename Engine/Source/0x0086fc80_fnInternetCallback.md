---
offset: "0x0086fc80"
module: "Engine/Source"
file: "Engine/Source/Os/Win64/OsURLDownload.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0086fc80 — `fnInternetCallback`

- **Адрес (Offset):** `0x0086fc80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Os/Win64/OsURLDownload.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0086fc80
static void CALLBACK fnInternetCallback(HINTERNET internet, DWORD_PTR context, DWORD internetStatus, LPVOID statusInformation, DWORD statusInformationLength) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0086fc80 в IDA Pro / Ghidra
