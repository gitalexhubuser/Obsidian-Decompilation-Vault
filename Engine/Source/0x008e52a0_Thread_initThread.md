---
offset: "0x008e52a0"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_thread.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008e52a0 — `Thread_initThread`

- **Адрес (Offset):** `0x008e52a0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_thread.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008e52a0
FMOD_RESULT Thread::initThread(const char *name, void (*func)(void *userdata), void *userdata, PRIORITY priority, void *stack, int stacksize, bool usesemaphore, int sleepperiod)
```

## Исследование и заметки
- [ ] Открыть адрес 0x008e52a0 в IDA Pro / Ghidra
