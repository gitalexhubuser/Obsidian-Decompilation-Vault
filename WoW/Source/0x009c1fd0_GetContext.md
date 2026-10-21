---
offset: "0x009c1fd0"
module: "WoW/Source"
file: "WoW/Source/Battlenet/BSN/BSNEncodeInterface.h"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x009c1fd0 — `GetContext`

- **Адрес (Offset):** `0x009c1fd0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Battlenet/BSN/BSNEncodeInterface.h`

## Сигнатура C++
```cpp
// OFFSET: 0x009c1fd0
template <class T, class P, int32_t ON_STACK> const BSN::EncodeContext* BSN::BSNEncodedObjectPtr<T, P, ON_STACK>::GetContext() const {
```

## Исследование и заметки
- [ ] Открыть адрес 0x009c1fd0 в IDA Pro / Ghidra
