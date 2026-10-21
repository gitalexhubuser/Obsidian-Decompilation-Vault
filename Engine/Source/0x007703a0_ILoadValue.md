---
offset: "0x007703a0"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SReg.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x007703a0 — `ILoadValue`

- **Адрес (Offset):** `0x007703a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SReg.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007703a0
static LSTATUS ILoadValue(HKEY parentkey, const char* subkeyname, const char* valuename, DWORD* datatype, void* buffer, DWORD bytes, DWORD* bytesread) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007703a0 в IDA Pro / Ghidra
