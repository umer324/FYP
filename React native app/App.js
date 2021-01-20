import React from "react";
import { StyleSheet, Text, View, Button } from "react-native";
import Ionicons from "react-native-vector-icons/Ionicons";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { createDrawerNavigator } from "@react-navigation/drawer";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

import DrawerContent from "./DrawerContent";

import SplashScreen from "./components/SplashScreen";
import Login from "./components/Login";
import Statistics from "./components/Statistics";
import Profile from "./components/Profile";
import ForgetPassword from "./components/ForgetPassword";
import MainTabScreen from "./MainTabScreen";
import AddSupervisor from "./components/supervisors/AddSupervisor";
import AddInspector from "./components/inspectors/AddInspector";

const Stack = createStackNavigator();
const Drawer = createDrawerNavigator();

export function Logout() {
  return <View></View>;
}

const HomeDrawer = (props) => {
  return (
    <Drawer.Navigator drawerContent={(props) => <DrawerContent {...props} />}>
      <Drawer.Screen name="Home" component={MainTabScreen} />
      <Drawer.Screen name="Profile" component={Profile} />
      <Drawer.Screen name="Statistics" component={Statistics} />
    </Drawer.Navigator>
  );
};

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="SplashScreen"
          component={SplashScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="AddSupervisor"
          component={AddSupervisor}
          options={{ headerShown: true }}
        />
        <Stack.Screen
          name="AddInspector"
          component={AddInspector}
          options={{ headerShown: true }}
        />
        <Stack.Screen
          name="Login"
          component={Login}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Home"
          component={HomeDrawer}
          options={{
            headerShown: false,
          }}
        />
        <Stack.Screen
          name="ForgetPassword"
          component={ForgetPassword}
          options={{ headerShown: false }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
