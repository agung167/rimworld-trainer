package com.rimworld.trainer.features;

import net.bytebuddy.ByteBuddy;
import net.bytebuddy.dynamic.DynamicType;
import net.bytebuddy.implementation.FixedValue;

import java.lang.reflect.Method;

public class GodMode {
    private static DynamicType.Unloaded<?> unloaded;

    public static void enable() {
        try {
            unloaded = new ByteBuddy()
                    .redefine(Class.forName("Verse.Pawn_HealthTracker"))
                    .method(named("ShouldBeDowned"))
                    .intercept(FixedValue.value(false))
                    .make();
            unloaded.load(GodMode.class.getClassLoader());
            System.out.println("God mode enabled.");
        } catch (Exception e) {
            System.err.println("Failed to enable god mode: " + e.getMessage());
        }
    }

    public static void disable() {
        if (unloaded != null) {
            unloaded.close();
            System.out.println("God mode disabled.");
        }
    }

    private static net.bytebuddy.matcher.ElementMatcher.Junction<Method> named(String name) {
        return net.bytebuddy.matcher.ElementMatchers.named(name);
    }
}