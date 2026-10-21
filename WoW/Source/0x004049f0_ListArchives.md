---
offset: "0x004049f0"
module: "WoW/Source"
file: "WoW/Source/Client.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004049f0 — `ListArchives`

- **Адрес (Offset):** `0x004049f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Client.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004049f0
static void ListArchives(const char* prefix, int32_t index, int32_t (*callback)(const char* fileName, void* param), void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004049f0 в IDA Pro / Ghidra
