---
offset: "0x004293e0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Version/Win64/Version.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004293e0 — `OsGetFileVersionInfoA`

- **Адрес (Offset):** `0x004293e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Version/Win64/Version.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004293e0
BOOL OsGetFileVersionInfoA(LPCSTR filename, DWORD handle, DWORD size, LPVOID data) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004293e0 в IDA Pro / Ghidra
