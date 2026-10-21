---
offset: "0x00439fe0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Log/Log.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00439fe0 — `System_Log_IVPrintf`

- **Адрес (Offset):** `0x00439fe0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Log/Log.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00439fe0
void System_Log::IVPrintf(bool locked, int32_t logClass, const char* name, const char* format, va_list args) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00439fe0 в IDA Pro / Ghidra
