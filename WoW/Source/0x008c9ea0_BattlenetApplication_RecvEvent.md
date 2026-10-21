---
offset: "0x008c9ea0"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c9ea0 — `BattlenetApplication_RecvEvent`

- **Адрес (Offset):** `0x008c9ea0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c9ea0
void BattlenetApplication::RecvEvent(const Battlenet::Event::Header& header, const BSN::EncodedObject* data) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c9ea0 в IDA Pro / Ghidra
