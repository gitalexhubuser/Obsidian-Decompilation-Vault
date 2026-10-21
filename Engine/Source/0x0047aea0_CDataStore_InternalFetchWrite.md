---
offset: "0x0047aea0"
module: "Engine/Source"
file: "Engine/Source/Base/CDataStore.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0047aea0 — `CDataStore_InternalFetchWrite`

- **Адрес (Offset):** `0x0047aea0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Base/CDataStore.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0047aea0
int32_t CDataStore::InternalFetchWrite(uint32_t pos, uint32_t bytes, uint8_t*& data, uint32_t& base, uint32_t& alloc, const char* fileName, int32_t lineNumber) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0047aea0 в IDA Pro / Ghidra
