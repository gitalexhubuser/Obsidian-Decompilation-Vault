---
offset: "0x00770580"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SReg.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00770580 — `InternalSaveEntry`

- **Адрес (Offset):** `0x00770580`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SReg.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00770580
static int32_t InternalSaveEntry(const char* keyname, const char* valuename, uint32_t flags, DWORD datatype, const void* buffer, DWORD bytes) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00770580 в IDA Pro / Ghidra
