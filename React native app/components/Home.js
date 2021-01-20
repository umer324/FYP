import React from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  FlatList,
  Alert,
  Button,
  ScrollView,
} from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { createDrawerNavigator } from "@react-navigation/drawer";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

import AddSupervisor from "./supervisors/AddSupervisor";
const supervisorImage = require("../icons/supervisor.png");
const inspectorImage = require("../icons/inspector.png");

export default function Home({ navigation }) {
  const renderSeparator = () => {
    return (
      <View
        style={{
          height: 1,
          width: "100%",
          backgroundColor: "#000",
        }}
      />
    );
  };
  const supervisorUserClick = (item) => {
    Alert.alert(item.key, "Supervisor");
  };

  const inspectorUserClick = (item) => {
    Alert.alert(item.key, "Inspector");
  };

  return (
    <ScrollView>
      <View style={styles.container}>
        <Text
          style={{
            fontSize: 20,
            paddingTop: 20,
            justifyContent: "center",
            paddingLeft: 10,
            fontStyle: "italic",
          }}
        >
          Supervisors :
        </Text>
        <View style={{ paddingTop: 30 }}>
          <FlatList
            data={[
              { key: "Abdul Khaliq" },
              { key: "Umer Imtiaz" },
              { key: "Abdul Muhib" },
              { key: "Zeeshan Choudhary" },
            ]}
            renderItem={({ item }) => (
              <Text
                style={styles.item}
                onPress={supervisorUserClick.bind(this, item)}
              >
                {item.key}
              </Text>
            )}
            ItemSeparatorComponent={renderSeparator}
          />
        </View>

        <Text
          style={{
            fontSize: 20,
            paddingTop: 20,
            justifyContent: "center",
            paddingLeft: 10,
            fontStyle: "italic",
          }}
        >
          Inspectors :
        </Text>
        <View style={{ paddingTop: 30 }}>
          <FlatList
            data={[{ key: "Abdul Wajid" }, { key: "Sajid" }, { key: "Maham" }]}
            renderItem={({ item }) => (
              <Text
                style={styles.item}
                onPress={inspectorUserClick.bind(this, item)}
              >
                {item.key}
              </Text>
            )}
            ItemSeparatorComponent={renderSeparator}
          />
        </View>

        <View style={styles.fixToText}>
          <Image
            source={supervisorImage}
            style={{ paddingLeft: 5, width: 110, height: 130 }}
          ></Image>
          <Image
            source={inspectorImage}
            style={{ paddingLeft: 5, width: 110, height: 130 }}
          ></Image>
        </View>
        <View style={styles.fixToText}>
          <Button
            title="Add Supervisor"
            onPress={() => navigation.navigate("AddSupervisor")}
          />
          <Button
            title="Add Inspector"
            onPress={() => navigation.navigate("AddInspector")}
          />
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  item: {
    padding: 10,
    fontSize: 18,
    height: 44,
    color: "white",
    backgroundColor: "skyblue",
  },
  fixToText: {
    paddingLeft: 10,
    paddingRight: 10,
    paddingTop: 20,
    flexDirection: "row",
    justifyContent: "space-between",
  },
});
