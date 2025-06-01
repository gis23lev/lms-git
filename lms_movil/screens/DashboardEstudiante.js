import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  Alert,
} from 'react-native';
import { useNavigation } from '@react-navigation/native';

export default function DashboardEstudiante() {
  const navigation = useNavigation();
  const [tareas, setTareas] = useState([]);
  const [loading, setLoading] = useState(true);

  const obtenerTareas = async () => {
    try {
      const response = await fetch('http://192.168.0.1:8000/api/tareas/');
      if (!response.ok) throw new Error('Error en la respuesta del servidor');

      const data = await response.json();
      setTareas(data);
    } catch (error) {
      Alert.alert('Error', 'No se pudieron obtener las tareas');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    obtenerTareas();
  }, []);

  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <Text style={styles.titulo}>{item.titulo}</Text>
      <Text style={styles.descripcion}>{item.descripcion}</Text>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('SubirArchivo', { tarea: item })}
      >
        <Text style={styles.buttonText}>Ver / Entregar</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Mis Tareas</Text>
      {loading ? (
        <ActivityIndicator size="large" color="#2B6CB0" />
      ) : tareas.length === 0 ? (
        <Text style={styles.empty}>No hay tareas asignadas aún.</Text>
      ) : (
        <FlatList
          data={tareas}
          keyExtractor={(item) => item.id || item._id?.$oid}
          renderItem={renderItem}
          contentContainerStyle={{ paddingBottom: 20 }}
        />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#E6F0FA',
    padding: 20,
    paddingTop: 40,
  },
  header: {
    fontSize: 26,
    fontWeight: 'bold',
    color: '#2B6CB0',
    marginBottom: 20,
    textAlign: 'center',
  },
  empty: {
    textAlign: 'center',
    marginTop: 40,
    fontSize: 16,
    color: '#4A5568',
  },
  card: {
    backgroundColor: '#fff',
    padding: 16,
    marginBottom: 16,
    borderRadius: 12,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 8,
    elevation: 4,
  },
  titulo: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#2D3748',
  },
  descripcion: {
    fontSize: 14,
    color: '#4A5568',
    marginVertical: 8,
  },
  button: {
    backgroundColor: '#2B6CB0',
    padding: 10,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 10,
  },
  buttonText: {
    color: '#fff',
    fontWeight: '600',
  },
});
