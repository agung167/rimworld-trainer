package com.rimworld.trainer.features;

import net.bytebuddy.ByteBuddy;
import net.bytebuddy.dynamic.DynamicType;
import net.bytebuddy.implementation.FixedValue;

import java.lang.reflect.Method;

public class InfiniteResources {
    private static DynamicType.Unloaded<?> unloaded;

    public static void enable() {
        try {
            unloaded = new ByteBuddy()
                    .redefine(Class.forName("RimWorld.Thing"))
                    .method(named("TakeDamage"))
                    .intercept(FixedValue.value(null))
                    .make();
            unloaded.load(InfiniteResources.class.getClassLoader());
            System.out.println("Infinite resources enabled.");
        } catch (Exception e) {
            System.err.println("Failed to enable infinite resources: " + e.getMessage());
        }
    }

    public static void disable() {
        if (unloaded != null) {
            unloaded.close();
            System.out.println("Infinite resources disabled.");
        }
    }

    private static net.bytebuddy.matcher.ElementMatcher.Junction<Method> named(String name) {
        return net.bytebuddy.matcher.ElementMatchers.named(name);
    }
}