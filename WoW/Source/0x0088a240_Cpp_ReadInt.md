---
offset: "0x0088a240"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/BSNCpp.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0088a240 — `Cpp_ReadInt`

- **Адрес (Offset):** `0x0088a240`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/BSNCpp.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0088a240
void BSN::Cpp::ReadInt(const void* data, uint32_t size, bool isSigned, uint64_t& value) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0088a240 в IDA Pro / Ghidra
