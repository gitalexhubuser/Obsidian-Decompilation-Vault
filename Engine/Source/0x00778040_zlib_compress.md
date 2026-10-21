---
offset: "0x00778040"
module: "Engine/Source"
file: "Engine/Source/Storm/Source/SComp.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00778040 — `zlib_compress`

- **Адрес (Offset):** `0x00778040`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Storm/Source/SComp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00778040
int32_t STORMAPI zlib_compress(uint8_t* dest, uint32_t* destLen, const uint8_t* source, uint32_t sourceLen, int32_t level) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00778040 в IDA Pro / Ghidra
