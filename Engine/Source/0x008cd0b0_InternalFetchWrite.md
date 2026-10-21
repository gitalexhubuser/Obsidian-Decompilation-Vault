---
offset: "0x008cd0b0"
module: "Engine/Source"
file: "Engine/Source/Base/CDataStore.h"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008cd0b0 — `InternalFetchWrite`

- **Адрес (Offset):** `0x008cd0b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Base/CDataStore.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008cd0b0
template <uint32_t size> int32_t CDataStoreCache<size>::InternalFetchWrite(uint32_t pos, uint32_t bytes, uint8_t*& data, uint32_t& base, uint32_t& alloc, const char* fileName, int32_t lineNumber) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cd0b0 в IDA Pro / Ghidra
