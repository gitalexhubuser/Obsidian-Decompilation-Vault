---
offset: "0x009aafb0"
module: "WoW/Common"
file: "WoW/Common/Lightning.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_common
---

# 0x009aafb0 — `CLightningManager_Add`

- **Адрес (Offset):** `0x009aafb0`
- **Модуль:** `WoW/Common`
- **Файл исходника:** `WoW/Common/Lightning.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009aafb0
uint32_t CLightningManager::Add(void (*coordUpdate)(void*, uint32_t, C3Vector*, C3Vector*), void* param, const SpellChainEffectsRec* chainEffects) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009aafb0 в IDA Pro / Ghidra
