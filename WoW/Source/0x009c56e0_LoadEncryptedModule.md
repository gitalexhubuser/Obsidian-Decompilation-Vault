---
offset: "0x009c56e0"
module: "WoW/Source"
file: "WoW/Source/Win64/BotCheck.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c56e0 — `LoadEncryptedModule`

- **Адрес (Offset):** `0x009c56e0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Win64/BotCheck.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c56e0
void LoadEncryptedModule(const uint8_t* key, uint32_t length, void (*callback)()) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c56e0 в IDA Pro / Ghidra
