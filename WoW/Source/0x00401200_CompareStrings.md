---
offset: "0x00401200"
module: "WoW/Source"
file: "WoW/Source/WowServices/PatchFiles.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00401200 — `CompareStrings`

- **Адрес (Offset):** `0x00401200`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/PatchFiles.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00401200
static int32_t CompareStrings(const void* a, const void* b, void* context) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00401200 в IDA Pro / Ghidra
