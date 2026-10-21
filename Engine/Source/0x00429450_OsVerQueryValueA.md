---
offset: "0x00429450"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Version/Win64/Version.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00429450 — `OsVerQueryValueA`

- **Адрес (Offset):** `0x00429450`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Version/Win64/Version.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00429450
BOOL OsVerQueryValueA(LPCVOID block, LPCSTR subBlock, LPVOID* buffer, PUINT length) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00429450 в IDA Pro / Ghidra
