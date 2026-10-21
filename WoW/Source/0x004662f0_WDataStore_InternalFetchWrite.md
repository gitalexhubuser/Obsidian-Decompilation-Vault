---
offset: "0x004662f0"
module: "WoW/Source"
file: "WoW/Source/WowServices/WDataStore.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004662f0 — `WDataStore_InternalFetchWrite`

- **Адрес (Offset):** `0x004662f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/WDataStore.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004662f0
int32_t WDataStore::InternalFetchWrite(uint32_t pos, uint32_t bytes, uint8_t*& data, uint32_t& base, uint32_t& alloc, const char* fileName, int32_t lineNumber) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004662f0 в IDA Pro / Ghidra
