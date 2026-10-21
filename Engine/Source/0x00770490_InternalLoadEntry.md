---
offset: "0x00770490"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/Win64/SReg.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00770490 — `InternalLoadEntry`

- **Адрес (Offset):** `0x00770490`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/Win64/SReg.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00770490
static int32_t InternalLoadEntry(const char* keyname, const char* valuename, uint32_t flags, DWORD* datatype, void* buffer, DWORD bytes, DWORD* bytesread) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00770490 в IDA Pro / Ghidra
