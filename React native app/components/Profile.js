import React from "react";
import { StyleSheet, Text, View, Image } from "react-native";

const logo = require("../icons/profile.png");

export default function ProfileScreen(props) {
  const { route, navigation } = props;
  const { item } = route.params;
  const { userEmail } = item;
  const userName = "Abdul Wajid";
  const role = "Admin";

  return (
    <View style={styles.container}>
      <View style={styles.header}></View>
      <Image style={styles.avatar} source={logo} />
      <View style={styles.body}>
        <View style={styles.bodyContent}>
          {/* Using Variables */}
          <Text style={styles.name}>{userName}</Text>
          <Text style={styles.info}>Role : {role}</Text>
          <Text style={styles.description}>Email : {userEmail}</Text>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  header: {
    backgroundColor: "#00BFFF",
    height: 200,
  },
  avatar: {
    width: 130,
    height: 130,
    borderRadius: 63,
    borderWidth: 4,
    borderColor: "white",
    marginBottom: 10,
    alignSelf: "center",
    position: "absolute",
    marginTop: 130,
  },
  name: {
    fontSize: 22,
    color: "#FFFFFF",
    fontWeight: "600",
  },
  body: {
    marginTop: 40,
  },
  bodyContent: {
    flex: 1,
    alignItems: "center",
    padding: 30,
  },
  name: {
    fontSize: 28,
    color: "#696969",
    fontWeight: "600",
  },
  info: {
    fontSize: 16,
    color: "#00BFFF",
    marginTop: 10,
  },
  description: {
    fontSize: 16,
    color: "#696969",
    marginTop: 50,
    textAlign: "center",
  },
});
