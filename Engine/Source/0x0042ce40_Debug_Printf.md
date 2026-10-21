---
offset: "0x0042ce40"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Debug/Debug.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0042ce40 — `Debug_Printf`

- **Адрес (Offset):** `0x0042ce40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Debug/Debug.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0042ce40
void Blizzard::Debug::Printf(void (*output)(const char*), const char* format, ...) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0042ce40 в IDA Pro / Ghidra
