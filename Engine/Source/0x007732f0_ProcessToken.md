---
offset: "0x007732f0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/SCmd.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x007732f0 — `ProcessToken`

- **Адрес (Offset):** `0x007732f0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/SCmd.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007732f0
static int32_t ProcessToken(const char* string, int32_t quoted, _PROCESSING* processing, CMDDEF** nextarg, int32_t (STORMAPI* extracallback)(const char*), void (STORMAPI* errorcallback)(_CMDERROR*)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007732f0 в IDA Pro / Ghidra
