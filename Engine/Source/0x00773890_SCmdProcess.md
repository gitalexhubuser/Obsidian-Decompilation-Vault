---
offset: "0x00773890"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/SCmd.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00773890 — `SCmdProcess`

- **Адрес (Offset):** `0x00773890`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/SCmd.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00773890
int32_t STORMAPI SCmdProcess(const char* cmdline, int32_t skipprogname, int32_t (STORMAPI* extracallback)(const char*), void (STORMAPI* errorcallback)(_CMDERROR*)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00773890 в IDA Pro / Ghidra
