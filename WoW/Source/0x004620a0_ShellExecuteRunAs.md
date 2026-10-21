---
offset: "0x004620a0"
module: "WoW/Source"
file: "WoW/Source/Glue/Win64/PatchDownloadGlue.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004620a0 — `ShellExecuteRunAs`

- **Адрес (Offset):** `0x004620a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/Win64/PatchDownloadGlue.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004620a0
static bool ShellExecuteRunAs(const char* path, const char* arguments) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004620a0 в IDA Pro / Ghidra
