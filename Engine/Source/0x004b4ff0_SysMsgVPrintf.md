---
offset: "0x004b4ff0"
module: "Engine/Source"
file: "Engine/Source/Services/SysMessage.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004b4ff0 — `SysMsgVPrintf`

- **Адрес (Offset):** `0x004b4ff0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/SysMessage.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004b4ff0
int32_t SysMsgVPrintf(STATUS_TYPE severity, uint32_t flags, const char* format, va_list args) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004b4ff0 в IDA Pro / Ghidra
