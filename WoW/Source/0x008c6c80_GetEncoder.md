---
offset: "0x008c6c80"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/BSNEncodeInterface.h"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c6c80 — `GetEncoder`

- **Адрес (Offset):** `0x008c6c80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/BSNEncodeInterface.h`

## Сигнатура C++
```cpp
// OFFSET: 0x008c6c80
template <class T, class P, int32_t ON_STACK> const BSN::PrimitiveEncoder* BSN::BSNEncodedObjectPtr<T, P, ON_STACK>::GetEncoder() const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c6c80 в IDA Pro / Ghidra
