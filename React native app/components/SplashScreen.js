import React, { Component, useEffect } from "react";
import { Button, Image, StatusBar, StyleSheet, Text, View } from "react-native";
import { TouchableOpacity } from "react-native-gesture-handler";
import Icon from "react-native-vector-icons/FontAwesome";
const logo = require("../icons/splashScreen.jpeg");
const arrowButton = require("../icons/rightArrow.png");

function SplashScreen({ navigation }) {
  useEffect(() => {
    window.setTimeout(async () => {
      navigation.navigate("Login");
    }, 5000);
  });
  return (
    <View style={styles.container}>
      <StatusBar
        barStyle="light-content"
        backgroundColor={styles.container.backgroundColor}
      />
      <Image style={styles.logo} source={logo}></Image>

      <TouchableOpacity
        style={{
          marginTop: 450,
          position: "relative",
          marginLeft: 230,
        }}
        onPress={() => navigation.navigate("Login")}
      >
        <Image source={arrowButton} style={{ width: 50, height: 50 }}></Image>
      </TouchableOpacity>
    </View>
  );
}

export default SplashScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "white",
  },
  welcome: {
    fontSize: 20,
    textAlign: "center",
    margin: 10,
    color: "#FFF",
    fontWeight: "bold",
  },
  logo: {
    paddingTop: 100,
    width: 310,
    height: 120,
  },
});
