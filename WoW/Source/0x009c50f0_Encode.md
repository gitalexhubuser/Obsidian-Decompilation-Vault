---
offset: "0x009c50f0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BattlenetProtocol.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c50f0 — `Encode`

- **Адрес (Offset):** `0x009c50f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BattlenetProtocol.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x009c50f0
int32_t ProtocolHard::TypeInfoOf<Battlenet::IP4::AddressPort>::Encode(const Battlenet::IP4::AddressPort& value, BSN::Hard::SizeEncoder& encoder) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c50f0 в IDA Pro / Ghidra
